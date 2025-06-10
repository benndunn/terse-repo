#!/usr/bin/env python
import typer
from typing import Optional

def main(who:Optional[str]=typer.Option("world", help="Who to say hello to")):
  
  print(f"Hello, {who}.")

if __name__=="__main__":
  typer.run(main)
        
