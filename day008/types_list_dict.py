def calculate_total(prices: list[int]) -> int:
    return sum(prices)
def get_student(name:str) -> dict[str, int]:
    return {"math": 90, "english": 85}
print(calculate_total([10, 20, 30]))
print(get_student("Alice")["math"])