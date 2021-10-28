#!/bin/sh
tmpfile_test='main.wast'
tmpfile_correct_wasm=$(echo $1 | sed -e 's/bin/wasm/g')
tmpfile_correct_wast=$(echo $1 | sed -e 's/bin/wast/g')
​
echo "> rars wasm.s pa $1"
rars wasm.s pa $1
​
echo "> rars WASMDisassembler.s pa main.wasm"
rars WASMDisassembler.s pa main.wasm > $tmpfile_test
​
echo "> rars WASMDisassembler.s pa $1"
rars WASMDisassembler.s pa $tmpfile_correct_wasm > $tmpfile_correct_wast
​
echo "> diff wast"
diff $tmpfile_test $tmpfile_correct_wast
​
echo "> diff wasm"
diff main.wasm $tmpfile_correct_wasm
​
rm -f $tmpfile_test $tmpfile_correct_wast