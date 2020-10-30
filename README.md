# gr-burstream

GNU Radio OOT module for inserting bursts of samples inside a stream.

Made following this instructions: https://wiki.gnuradio.org/index.php/OutOfTreeModules

* `gr_modtool newmod burstream`
* `$ gr_modtool add --block-type source --add-python-qa --lang python burstreamer_c`
    ```
    GNU Radio module name identified: burstream
    Language: Python
    Block/code identifier: burstreamer_c
    Please specify the copyright holder: Francisco Albani
    Enter valid argument list, including default arguments: 
    Adding file 'python/burstreamer_c.py'...
    Adding file 'python/qa_burstreamer_c.py'...
    Editing python/CMakeLists.txt...
    Adding file 'grc/burstream_burstreamer_c.block.yml'...
    Editing grc/CMakeLists.txt...
    ```
