class Chunker:
    def __init__(self, chunk_size: int = 12):
        """
        Initialize the Chunker with a specified chunk size.
        chunk_size ကို သတ်မှတ်၍ Chunker ကို စတင်ခြင်း။
        """
        self.chunk_size = chunk_size

    def to_chunks(self, plaintext: str) -> list[list[int]]:
        """
        Split plaintext into chunks and convert each chunk into low-level integer array (Bytes).
        Input စာသားကို chunk_size အလိုက် အပိုင်းခွဲမည်။ ပြီးလျှင် Low-level integer array (Bytes) သို့ ပြောင်းမည်။
        """
        # 1. Split string into chunks / စာသားကို သတ်မှတ်အရွယ်အစားအလိုက် အပိုင်းခွဲခြင်း
        string_chunks = [
            plaintext[i : i + self.chunk_size]
            for i in range(0, len(plaintext), self.chunk_size)
        ]

        # 2. Convert each chunk into low-level integer array (Bytes) / အပိုင်းတစ်ခုချင်းစီကို byte array သို့ ပြောင်းခြင်း
        low_level_chunks = [list(chunk.encode('utf-8')) for chunk in string_chunks]
        return low_level_chunks