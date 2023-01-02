# Timestamps in readable format, touch folders/files with timestamp 


```python
# Tested with:
# Python 3.9.13
# Windows 10


$pip install files-folders-with-timestamp



from files_folders_with_timestamp import get_timestamp, create_file_with_timestamp, create_folder_with_timestamp
print(get_timestamp(sep="_"))
print(create_file_with_timestamp(folder=None, extension='.tmp', prefix='bild___', suffix='', sep='_', create_file=False))
print(create_file_with_timestamp(folder='f:\\testes\\dddd\\sasa', extension='.tmp', prefix='', suffix='', sep='-', create_file=True))
print(create_folder_with_timestamp(folder='f:\\newfolder', prefix='b', suffix='x', sep='_', create_folder=False))
print(create_folder_with_timestamp(folder='f:\\newfolder2', prefix='b', suffix='x', sep='x', create_folder=True))



2023_01_01_22_21_30_438475
bild___2023_01_01_22_21_30_438475.tmp
f:\testes\dddd\sasa\2023-01-01-22-21-30-438475.tmp
f:\newfolder\b2023_01_01_22_21_30_450186x
f:\newfolder2\b2023x01x01x22x21x30x451162x

	
```




