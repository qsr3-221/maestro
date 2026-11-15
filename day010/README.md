# CLI Task Manager

## 运行
```bash
cd ~/maestro/day010
python3 -m task_manager.main
```
## 测试
```bash
cd ~/maestro/day010
python3 -m unittest test_manager
```
## 数据持久化
- 任务保存在 `tasks.json`。
- 退出时自动保存，启动时自动加载。
- 加载后是 `Task` 对象，不是 `dict`。
