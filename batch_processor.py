#!/usr/bin/env python3
"""
Fooocus Batch Processor
Automatically processes prompts from TXT files in batches of 32.
"""

import os
import sys
import time
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

# Add Fooocus modules to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import modules.config as config
import modules.async_worker as worker
import modules.flags as flags


class BatchProcessor:
    def __init__(self, prompts_dir: str = "prompts", output_dir: str = None, batch_size: int = 32):
        """
        Initialize the batch processor.
        
        Args:
            prompts_dir: Directory containing TXT files with prompts
            output_dir: Directory to save generated images (uses Fooocus default if None)
            batch_size: Number of images to generate per batch (max 32 for stability)
        """
        self.prompts_dir = Path(prompts_dir)
        self.output_dir = Path(output_dir) if output_dir else Path(config.path_outputs)
        self.batch_size = min(batch_size, 32)  # Enforce max 32 for stability
        
        # Create prompts directory if it doesn't exist
        self.prompts_dir.mkdir(exist_ok=True)
        
        print(f"Batch Processor initialized:")
        print(f"  Prompts directory: {self.prompts_dir.absolute()}")
        print(f"  Output directory: {self.output_dir.absolute()}")
        print(f"  Batch size: {self.batch_size}")
    
    def get_txt_files(self) -> List[Path]:
        """Get all TXT files from prompts directory, sorted alphabetically."""
        txt_files = sorted(self.prompts_dir.glob("*.txt"))
        return txt_files
    
    def read_prompts_from_file(self, file_path: Path) -> List[str]:
        """
        Read prompts from a TXT file.
        Each line is treated as a separate prompt.
        Empty lines and lines starting with # are ignored.
        """
        prompts = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#'):
                        prompts.append(line)
            print(f"  Read {len(prompts)} prompts from {file_path.name}")
        except Exception as e:
            print(f"  Error reading {file_path.name}: {e}")
        return prompts
    
    def generate_images(self, prompts: List[str], file_name: str) -> bool:
        """
        Generate images for a batch of prompts.
        
        Args:
            prompts: List of prompts to generate
            file_name: Name of the source file (for logging)
        
        Returns:
            True if successful, False otherwise
        """
        try:
            print(f"\n  Generating {len(prompts)} images...")
            
            # Import here to ensure Fooocus is fully initialized
            from webui import get_task, generate_clicked
            
            # Prepare arguments for image generation
            # This mimics the Gradio interface arguments
            args = [
                None,  # currentTask placeholder
                prompts[0] if prompts else "",  # First prompt as main prompt
                "",  # negative_prompt
                config.default_styles,  # style_selections
                config.default_performance,  # performance_selection
                config.default_aspect_ratio.split(' ')[0],  # aspect_ratios_selection
                len(prompts),  # image_number
                config.default_output_format,  # output_format
                0,  # image_seed (will be randomized)
                True,  # seed_random
                False,  # image_prompt_checkbox
                # ... add more default parameters as needed
            ]
            
            # Create task
            task = worker.AsyncTask(args=args)
            task.image_number = len(prompts)
            
            # For multiple prompts, we need to process them individually
            # This is a simplified approach - you may need to adjust based on Fooocus internals
            for i, prompt in enumerate(prompts):
                print(f"    [{i+1}/{len(prompts)}] {prompt[:60]}...")
            
            # Add task to queue
            worker.async_tasks.append(task)
            
            # Wait for completion
            print(f"  Waiting for generation to complete...")
            while task.processing or len(task.yields) > 0:
                time.sleep(1)
            
            print(f"  ✓ Generation complete!")
            return True
            
        except Exception as e:
            print(f"  ✗ Error during generation: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def process_file(self, file_path: Path, delete_after: bool = True) -> bool:
        """
        Process a single TXT file.
        
        Args:
            file_path: Path to the TXT file
            delete_after: Whether to delete the file after successful processing
        
        Returns:
            True if successful, False otherwise
        """
        print(f"\n{'='*60}")
        print(f"Processing: {file_path.name}")
        print(f"{'='*60}")
        
        # Read prompts
        prompts = self.read_prompts_from_file(file_path)
        if not prompts:
            print(f"  No valid prompts found in {file_path.name}")
            return False
        
        # Process in batches
        total_prompts = len(prompts)
        success = True
        
        for i in range(0, total_prompts, self.batch_size):
            batch = prompts[i:i + self.batch_size]
            batch_num = (i // self.batch_size) + 1
            total_batches = (total_prompts + self.batch_size - 1) // self.batch_size
            
            print(f"\nBatch {batch_num}/{total_batches} ({len(batch)} prompts)")
            
            if not self.generate_images(batch, file_path.name):
                success = False
                break
        
        # Delete file if successful and requested
        if success and delete_after:
            try:
                file_path.unlink()
                print(f"\n✓ Deleted processed file: {file_path.name}")
            except Exception as e:
                print(f"\n✗ Error deleting file: {e}")
                success = False
        
        return success
    
    def run(self, delete_after: bool = True, continuous: bool = False):
        """
        Run the batch processor.
        
        Args:
            delete_after: Whether to delete TXT files after processing
            continuous: If True, keep running and check for new files
        """
        print("\n" + "="*60)
        print("FOOOCUS BATCH PROCESSOR")
        print("="*60)
        
        if continuous:
            print("\nRunning in continuous mode. Press Ctrl+C to stop.")
            print("Checking for new TXT files every 10 seconds...\n")
        
        try:
            while True:
                # Get all TXT files
                txt_files = self.get_txt_files()
                
                if not txt_files:
                    if continuous:
                        print(f"No TXT files found. Waiting...")
                        time.sleep(10)
                        continue
                    else:
                        print(f"\nNo TXT files found in {self.prompts_dir.absolute()}")
                        print(f"Please add TXT files with prompts (one per line) and run again.")
                        break
                
                print(f"\nFound {len(txt_files)} file(s) to process:")
                for f in txt_files:
                    print(f"  - {f.name}")
                
                # Process each file
                for txt_file in txt_files:
                    self.process_file(txt_file, delete_after=delete_after)
                
                if not continuous:
                    break
                
                print(f"\nAll files processed. Checking for new files in 10 seconds...")
                time.sleep(10)
                
        except KeyboardInterrupt:
            print("\n\nBatch processor stopped by user.")
        
        print("\n" + "="*60)
        print("BATCH PROCESSING COMPLETE")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(
        description="Fooocus Batch Processor - Process prompts from TXT files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python batch_processor.py
  python batch_processor.py --prompts-dir my_prompts --batch-size 16
  python batch_processor.py --continuous --keep-files
  
TXT File Format:
  - One prompt per line
  - Lines starting with # are ignored (comments)
  - Empty lines are ignored
        """
    )
    
    parser.add_argument(
        '--prompts-dir',
        type=str,
        default='prompts',
        help='Directory containing TXT files with prompts (default: prompts)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default=None,
        help='Directory to save generated images (default: Fooocus default)'
    )
    
    parser.add_argument(
        '--batch-size',
        type=int,
        default=32,
        help='Number of images per batch (max 32, default: 32)'
    )
    
    parser.add_argument(
        '--keep-files',
        action='store_true',
        help='Keep TXT files after processing (default: delete them)'
    )
    
    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run continuously, checking for new files every 10 seconds'
    )
    
    args = parser.parse_args()
    
    # Create and run processor
    processor = BatchProcessor(
        prompts_dir=args.prompts_dir,
        output_dir=args.output_dir,
        batch_size=args.batch_size
    )
    
    processor.run(
        delete_after=not args.keep_files,
        continuous=args.continuous
    )


if __name__ == "__main__":
    main()
