import re
import shutil
from pathlib import Path

from fill_gaps import fill_gaps

expected_sequence = ('spam001.txt',
                     'spam002.txt',
                     'spam003.txt',
                     'spam004.txt',
                     'spam005.txt',
                     'spam006.txt',
                     'spam007.txt',
                     'spam008.txt',
                     'spam009.txt',
                     'spam010.txt')
expected_gaps = ('spam001.txt',
                 'spam003.txt',
                 'spam005.txt',
                 'spam007.txt',
                 'spam009.txt',
                 'spam011.txt',
                 'spam013.txt',
                 'spam015.txt',
                 'spam017.txt',
                 'spam019.txt')
expected_gap = ('spam001.txt',
                'spam002.txt',
                'spam003.txt',
                'spam004.txt',
                'spam008.txt',
                'spam009.txt',
                'spam010.txt',
                'spam011.txt',
                'spam012.txt',
                'spam013.txt')


def test_get_matching_files():
    expected_matches = ('__init__.py',
                        'fill_gaps.py',
                        'test_fill_gaps.py')

    root = Path('./fill_gaps/').resolve()

    matches = fill_gaps.get_matching_files(root=root,
                                           regex=re.compile(r'(^.*)(\.py$)'))
    py_files = sorted([file.name for file in root.glob('*.py')])

    assert len(matches) == len(expected_matches)
    assert len(py_files) == len(matches)

    for match in matches:
        assert match in expected_matches
        assert match in py_files


def test_fill_sequence_gap():
    # dir at path created
    root = Path('./fill_gaps/test_files').resolve()
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)

    # creates files with only odd numbers spam00<x>.txt
    for x in range(1, 20, 2):
        with open(root / f'spam{x:03}.txt', 'w') as spam:
            spam.write(f'spam{x:03d}')

    # files created prior to filling gaps
    gap_files = [file.name for file in root.iterdir() if file.is_file()]
    for gap_file in gap_files:
        assert gap_file in expected_gaps

    # results after filling gaps
    fill_gaps.fill_sequence_gap(root, 'spam', '.txt')
    fill_files = [file.name for file in root.iterdir()]
    regex = re.compile(r'(^spam)(\d+)(.*)?(\.txt$)')

    # verifies files are renamed as expected and file contents remain unchanged
    for fill_file in fill_files:
        assert fill_file in expected_sequence
        with root.joinpath(fill_file).open('r') as reader:
            file_num = int(regex.search(fill_file).group(2))
            assert reader.read() == f'spam{(file_num * 2) - 1:03d}'

    # removes dir and it's contents (to ensure consistent test results)
    shutil.rmtree(root)


def test_insert_gap():
    # dir at path created
    root = Path('./fill_gaps/test_files').resolve()
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)

    # creates files with sequential numbers spam00<x>.txt
    for x in range(1, 11):
        with open(root / f'spam{x:03}.txt', 'w') as spam:
            spam.write(f'spam{x:03d}')

    # results prior to inserting gap
    for file in root.iterdir():
        assert file.name in expected_sequence

    # results after inserting gap
    fill_gaps.insert_gap(root, 'spam', '.txt', 5, 8)
    regex = re.compile(r'(^spam)(\d+)(.*)?(\.txt$)')

    # verifies files are renamed as expected and file contents remain unchanged
    for gap_file in root.iterdir():
        assert gap_file.name in expected_gap
        with open(root / gap_file, 'r') as reader:
            file_num = int(regex.search(gap_file.name).group(2))
            text = f'spam{file_num if file_num < 5 else file_num - 3:03d}'
            assert reader.read() == text

    # removes dir and it's contents (to ensure consistent test results)
    shutil.rmtree(root)
