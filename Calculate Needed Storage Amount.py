# Use floor division to calculate how many blocks are fully occupied
# Use the modulo operator to check whether there's any remainder
# Depending on whether there's a remainder or not, return
# the total number of bytes required to allocate enough blocks to store your data.


def calculate_storage(filesize):
  block_size = 4096
  
  full_blocks = filesize//block_size
 
  partial_block_remainder = filesize%block_size
 
  if partial_block_remainder > 0:
    return block_size*full_blocks+block_size
  return block_size*full_blocks

print(calculate_storage(int(input("enter file size"))))