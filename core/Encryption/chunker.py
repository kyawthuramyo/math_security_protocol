class DataChunker:
    def __init__(self, chunk_size: int = 16):
        """
        Initialize the Chunker with a specified chunk size.
        chunk_size ကို သတ်မှတ်၍ DataChunker ကို စတင်ခြင်း။
        """
        self.chunk_size = chunk_size

    def text_to_low_level_chunks(self, plaintext: str) -> list[list[int]]:
        """
        Split plaintext into chunks and convert each chunk into low-level integer arrays (Bytes).
        Input စာသားကို chunk_size အလိုက် အပိုင်းခွဲမည်၊ ပြီးလျှင် Low-level integer array (Bytes) များအဖြစ်သို့ ပြောင်းမည်။
        """
        # 1. Split string into chunks / စာသားကို သတ်မှတ်အရွယ်အစားအလိုက် အပိုင်းခွဲခြင်း
        string_chunks = [
            plaintext[i : i + self.chunk_size]
            for i in range(0, len(plaintext), self.chunk_size)
        ]
        
        # 2. Convert each chunk into low-level integer array (Bytes) / အပိုင်းတစ်ခုချင်းစီကို Low-level Integer Array သို့ ပြောင်းခြင်း
        low_level_chunks = [list(chunk.encode('utf-8')) for chunk in string_chunks]
        return low_level_chunks