# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
  """Thêm một công việc mới vào danh sách."""
  tasks.append(task_name)
  print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
  print("Chào mừng đến với ứng dụng To-Do List!")
  add_task("Học bài Git và GitHub")
  add_task("Làm bài tập thực hành ở nhà")

# Liệt kê tất cả các công việc 
tasks = []  # ví dụ: ["Học Git", "Làm bài tập"]
def add_task(name: str):
    tasks.append(name)
def list_tasks():
    if not tasks:
        print("Chưa có công việc nào.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

