from transformers import AutoTokenizer

colors_list = [
    '102;194;165', '252;141;98', '141;160;203', 
    '231;138;195', '166;216;84', '255;217;47'
]

def show_tokens(sentence, tokenizer_name):
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    token_ids = tokenizer(sentence).input_ids
    for idx, t in enumerate(token_ids):
        print(
            f'\x1b[0;30;48;2;{colors_list[idx % len(colors_list)]}m' + 
            tokenizer.decode(t) + 
            '\x1b[0m', 
            end=' '
        )