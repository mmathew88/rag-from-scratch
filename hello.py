import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Mean: {arr.mean()}")

df = pd.DataFrame({
    "question": ["What is RAG?", "What is an embedding?"],
    "difficulty": ["easy", "medium"]
})
print("\nDataFrame:")
print(df)

print("\n✅ Environment working!")