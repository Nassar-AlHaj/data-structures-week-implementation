from dynamic_array import MyDynamicArray

print("=== Testing MyDynamicArray ===")

# إنشاء Array جديدة
arr = MyDynamicArray()

# إضافة عناصر
arr.add(1)
arr.add(2)
arr.add(3)
print("Array بعد الإضافة:", arr)  # [1, 2, 3]

# اختبار get و set
print("Get index 1:", arr.get(1))  # 2
arr.set(1, 99)
print("بعد set index 1:", arr)  # [1, 99, 3]

# اختبار remove_at
removed = arr.remove_at(1)
print("تم إزالة:", removed)  # 99
print("بعد remove_at:", arr)  # [1, 3]

# اختبار remove
arr.add(5)
print("قبل remove 3:", arr)  # [1, 3, 5]
arr.remove(3)
print("بعد remove 3:", arr)  # [1, 5]

# اختبار contains و index_of
print("Contains 5?", arr.contains(5))  # True
print("Index of 5:", arr.index_of(5))  # 1

# اختبار clear
arr.clear()
print("بعد clear:", arr)  # []

# اختبار is_empty و size
print("Is empty?", arr.is_empty())  # True
print("Size:", arr.size())  # 0

print("\n✅ All MyDynamicArray tests passed!")
