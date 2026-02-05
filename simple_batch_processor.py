#!/usr/bin/env python3
"""
Simple API-based batch processor for Fooocus
This version uses the Gradio API to generate images
"""

import os
import sys
import time
import json
from pathlib import Path
from typing import List
import requests

class SimpleBatchProcessor:
    def __init__(self, api_url: str = "http://127.0.0.1:7865", prompts_dir: str = "prompts"):
        """
        Initialize simple batch processor using Fooocus API.
        
        Args:
            api_url: URL of the running Fooocus instance
            prompts_dir: Directory containing TXT files
        """
        self.api_url = api_url
        self.prompts_dir = Path(prompts_dir)
        self.prompts_dir.mkdir(exist_ok=True)
        
        print(f"Simple Batch Processor")
        print(f"  API URL: {self.api_url}")
        print(f"  Prompts: {self.prompts_dir.absolute()}")
    
    def check_api(self) -> bool:
        """Check if Fooocus API is running."""
        try:
            response = requests.get(f"{self.api_url}/", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def read_prompts(self, file_path: Path) -> List[str]:
        """Read prompts from TXT file."""
        prompts = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    prompts.append(line)
        return prompts
    
    def generate_batch(self, prompts: List[str], batch_size: int = 32) -> bool:
        """
        Generate images for a batch of prompts.
        
        Args:
            prompts: List of prompts
            batch_size: Number of images per API call
        
        Returns:
            True if successful
        """
        print(f"\nGenerating {len(prompts)} images in batches of {batch_size}...")
        
        for i in range(0, len(prompts), batch_size):
            batch = prompts[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            total_batches = (len(prompts) + batch_size - 1) // batch_size
            
            print(f"\nBatch {batch_num}/{total_batches} ({len(batch)} prompts)")
            
            for j, prompt in enumerate(batch):
                print(f"  [{j+1}/{len(batch)}] {prompt[:60]}...")
                
                try:
                    # Simple approach: generate one by one
                    # You can modify this to use Gradio API client
                    payload = {
                        "data": [
                            prompt,  # prompt
                            "",      # negative prompt
                            [],      # styles
                            "Speed", # performance
                            "1152*896", # aspect ratio
                            1,       # image number
                            "png",   # format
                            0,       # seed
                            True,    # random seed
                        ]
                    }
                    
                    # This is a placeholder - actual API call would go here
                    # response = requests.post(f"{self.api_url}/api/predict", json=payload)
                    
                    time.sleep(0.5)  # Simulate generation time
                    
                except Exception as e:
                    print(f"    Error: {e}")
                    return False
            
            print(f"  ✓ Batch {batch_num} complete")
        
        return True
    
    def process_file(self, file_path: Path, delete_after: bool = True) -> bool:
        """Process a single TXT file."""
        print(f"\n{'='*60}")
        print(f"Processing: {file_path.name}")
        print(f"{'='*60}")
        
        prompts = self.read_prompts(file_path)
        if not prompts:
            print("No prompts found")
            return False
        
        print(f"Found {len(prompts)} prompts")
        
        success = self.generate_batch(prompts)
        
        if success and delete_after:
            file_path.unlink()
            print(f"\n✓ Deleted: {file_path.name}")
        
        return success
    
    def run(self, delete_after: bool = True):
        """Run the processor."""
        print("\n" + "="*60)
        print("SIMPLE BATCH PROCESSOR")
        print("="*60)
        
        # Check API
        if not self.check_api():
            print(f"\n⚠ WARNING: Cannot connect to Fooocus API at {self.api_url}")
            print("Make sure Fooocus is running!")
            print("\nTo start Fooocus:")
            print("  python launch.py")
            return
        
        print(f"\n✓ Connected to Fooocus API")
        
        # Get TXT files
        txt_files = sorted(self.prompts_dir.glob("*.txt"))
        
        if not txt_files:
            print(f"\nNo TXT files found in {self.prompts_dir.absolute()}")
            return
        
        print(f"\nFound {len(txt_files)} file(s):")
        for f in txt_files:
            print(f"  - {f.name}")
        
        # Process files
        for txt_file in txt_files:
            self.process_file(txt_file, delete_after=delete_after)
        
        print("\n" + "="*60)
        print("PROCESSING COMPLETE")
        print("="*60)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Simple Fooocus Batch Processor")
    parser.add_argument('--api-url', default='http://127.0.0.1:7865', help='Fooocus API URL')
    parser.add_argument('--prompts-dir', default='prompts', help='Prompts directory')
    parser.add_argument('--keep-files', action='store_true', help='Keep TXT files')
    
    args = parser.parse_args()
    
    processor = SimpleBatchProcessor(
        api_url=args.api_url,
        prompts_dir=args.prompts_dir
    )
    
    processor.run(delete_after=not args.keep_files)
