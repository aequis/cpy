# cpy_utils

These two scripts let you store a bunch of file paths that you want to copy to a destination in a separate step. They work with files and directories.

Example (script has been aliased to cpy and pst):  
cpy file1 file2 file3  
z proj/s  
pst .  

This fills a *very* specific need I had, so probably not useful to anybody else. 

I'm tired of typing out endlessly long file paths and I'm incredibly unhappy with how file managers navigate directory trees. It's a lot of manual clicking back and forth. Also, bookmarks/favourites are such an awkward solution, and it's something I've largely replaced with rupa/z. z tracks which directories I go to and allows me to use extremely short arguments to reach whatever directories I've been to. Instead of "cd ~/src/python/project/src/", I can just do something like "z project/s" and it jumps to it immediately.

This allows me to copy a bunch of file(paths)s, use z to reach the destination and paste it there instead of endlessly traversing through a directory tree with a GUI or something like:  
cp file1 ~/path/to/some/deep/dir  
cp file2 ~/path/to/some/deep/dir  
cp file3 ~/path/to/some/other/deep/dir  

This is an early version and I'm thinking about ways to extend it. Maybe I can integrate z somehow? Or add similar functionality? So I can just do something like "cpy file1 file2 file3 z ep/dir".
