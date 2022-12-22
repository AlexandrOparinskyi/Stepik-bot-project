BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 1500

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end: int = 0
    if len(text) < start + size:
        return text[start::], size - (size + start - len(text))
    for i in range(size + start - 1, 1, -1):
        if text[i] in ',.!:;?':
            if text[i + 1] in ',.!:;?' or text[i - 1] in ',.!:;?':
                continue
            else:
                end = i
                break
    return text[start:end + 1], end - start + 1


def prepare_book(path: str) -> None:
    count = 1
    start = 0
    with open(path, encoding='utf-8') as book_file:
        f = book_file.read()
        while True:
            func = _get_part_text(f, start, PAGE_SIZE)
            if not func[0]:
                break
            book[count] = func[0].lstrip()
            count += 1
            start += func[1]


prepare_book(BOOK_PATH)
