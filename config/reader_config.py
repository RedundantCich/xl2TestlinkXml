# file format -> xlsx or xls
file_format = 'xlsx'

# rows to skip -> you should include headers here
# For example if 1 is empty and 2 is headers, you should write in 2
rows_to_skip = 2

# columns in use -> You can change the main keys to have them the same
# as your excel files
columns_in_use = {
    'B': {
        'txt_name': 'testsuite',
        'role': 'main_test_suite'
        },
    'C': {
        'txt_name': 'testsuite',
        'role': 'sub_test_suite'
        },
    'D': {
        'txt_name': 'testcase',
        'role': 'test_case'
        },
    'E': {
        'txt_name': 'importance',
        'role': 'in_between'
        },
    'F': {
        'txt_name': 'summary',
        'role': 'in_between'
        },
    'G': {
        'txt_name': 'preconditions',
        'role': 'preconditions'
        },
    'H': {
        'txt_name': 'actions',
        'role': 'actions'
        },
    'I': {
        'txt_name': 'expectedresults',
        'role': 'expected_results'
        }
}
