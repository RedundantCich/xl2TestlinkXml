# Excel to XML for Testlink
# xl_to_xml_for_testlink

## Description

This is a little script to convert .xlsx/.xls files with your test suites into .xml in order to import them into TestLink.

I find it more relaxing and efficient to write test cases in LibreOffice Calc, but TestLink is definitely more useful
for planning and executing test scenarios.

There is an example xlsx file in ./xl_source/

## Prerequisites

1. The script uses openpyxl for reading excel files.
    You can just run the following command:

    pip install openpyxl

2. Put your excel files containing your test suites into ./xl_source/ folder.

3. Go to ./config/reader_config.py and edit the file:

    rows_to_skip = int with the number of the row where your data starts
    file_format = 'xlsx' or 'xls'
    columns_in_use = set the columns you use as keys according to value[0]

## Running

Just run: 

    exec_script.py

The results will be in ./xml_results/
