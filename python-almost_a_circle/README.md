Python - Almost a circle

python3 -c 'print(__import__("base").__doc__)'

python3 -c 'print(__import__("base").Base.__doc__)'

python3 -c 'print(__import__("rectangle").__doc__)'

python3 -c 'print(__import__("rectangle").Rectangle.__doc__)'

python3 -c 'print(__import__("square").__doc__)'

python3 -c 'print(__import__("square").Square.__doc__)'

python3 -c 'print(__import__("base").__init__.__doc__)'

python3 -c 'print(__import__("base").to_json_string.__doc__)'

python3 -c 'print(__import__("base").save_to_file.__doc__)'

python3 -c 'print(__import__("base").from_json_string.__doc__)'

python3 -c 'print(__import__("base").create.__doc__)'

python3 -c 'print(__import__("base").load_from_file.__doc__)'

python3 -c 'print(__import__("base").save_to_file_csv.__doc__)'

python3 -c 'print(__import__("base").load_from_file_csv.__doc__)'

python3 -c 'print(__import__("base").draw.__doc__)'
