#!/usr/bin/env python3
"""
Fooocus Batch Processor - Standalone Version
Automatically processes prompts from TXT files and calls Fooocus for generation.
"""

import os
import sys
import time
import subprocess
import argparse
from pathlib import Path
from typing import List

class StandaloneBatchProcessor:
    def __init__(self, prompts_dir: str = "prompts", batch_size: int = 32):
        """
        Initialize the standalone batch processor.
        
        Args:
            prompts_dir: Directory containing TXT files with prompts
            batch_size: Number of prompts per batch (max 32)
        """
        self.prompts_dir = Path(prompts_dir)
        self.batch_size = min(batch_size, 32)
        
        # Create prompts directory if it doesn't exist
        self.prompts_dir.mkdir(exist_ok=True)
        
        print(f"Standalone Batch Processor initialized:")
        print(f"  Prompts directory: {self.prompts_dir.absolute()}")
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
    
    def create_batch_file(self, prompts: List[str], batch_num: int) -> Path:
        """Create a temporary batch file for processing."""
        batch_file = self.prompts_dir / f"_batch_{batch_num:03d}.txt"
        with open(batch_file, 'w', encoding='utf-8') as f:
            for prompt in prompts:
                f.write(f"{prompt}\n")
        return batch_file
    
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
        
        print(f"\nTotal prompts: {total_prompts}")
        print(f"Will process in {(total_prompts + self.batch_size - 1) // self.batch_size} batch(es)")
        print(f"\nNOTE: This is a standalone processor.")
        print(f"For actual image generation, you need to:")
        print(f"  1. Start Fooocus: python launch.py")
        print(f"  2. Use the web interface to generate images")
        print(f"  3. Or use the API-based simple_batch_processor.py")
        
        # Show all prompts
        print(f"\nPrompts to generate:")
        for i, prompt in enumerate(prompts, 1):
            print(f"  [{i:3d}] {prompt}")
        
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
        print("FOOOCUS STANDALONE BATCH PROCESSOR")
        print("="*60)
        print("\nThis version lists prompts from TXT files.")
        print("For actual generation, use one of these methods:")
        print("  1. Copy prompts to Fooocus web interface")
        print("  2. Use simple_batch_processor.py with running Fooocus")
        print("  3. Modify this script to integrate with Fooocus API")
        
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
        description="Fooocus Standalone Batch Processor - List prompts from TXT files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python standalone_batch_processor.py
  python standalone_batch_processor.py --prompts-dir my_prompts
  python standalone_batch_processor.py --continuous --keep-files
  
TXT File Format:
  - One prompt per line
  - Lines starting with # are ignored (comments)
  - Empty lines are ignored

NOTE: This standalone version only reads and displays prompts.
For actual image generation, use:
  - simple_batch_processor.py (requires running Fooocus)
  - Or copy prompts to Fooocus web interface manually
        """
    )
    
    parser.add_argument(
        '--prompts-dir',
        type=str,
        default='prompts',
        help='Directory containing TXT files with prompts (default: prompts)'
    )
    
    parser.add_argument(
        '--batch-size',
        type=int,
        default=32,
        help='Number of prompts per batch (max 32, default: 32)'
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
    processor = StandaloneBatchProcessor(
        prompts_dir=args.prompts_dir,
        batch_size=args.batch_size
    )
    
    processor.run(
        delete_after=not args.keep_files,
        continuous=args.continuous
    )


if __name__ == "__main__":
    main()
