class GlobalReverseTransformer:
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def reverse_global(self, shuffled_chunks: list[list[int]], shuffle_metadata: list[int]) -> list[list[int]]:
        restored_chunks = []

        for i in range(0, len(shuffled_chunks), self.batch_size):
            current_batch_chunks = shuffled_chunks[i:i + self.batch_size]
            current_weights = shuffle_metadata[i:i + self.batch_size]
            batch_len = len(current_batch_chunks)

            paired = list(zip(current_weights, current_batch_chunks))
            paired.sort(key=lambda x: x[0], reverse=True)

            original_batch = [item[1] for item in paired]
            restored_chunks.extend(original_batch)

        return restored_chunks