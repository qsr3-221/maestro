# HTTP / REST 基础

## 1. 请求与响应
客户端发请求给服务器，服务器响应客户端
请求包含方法，路径，请求头，请求体
响应包含状态码、响应头、响应体

## 2. 常见方法

| 方法 | 语义 | CLI 对应 |
|---|---|---|
| GET | 读取资源 | `show()` 查看任务 |
| POST | 创建资源 | `add()` 添加任务 |
| PUT | 更新资源 | 暂无 |
| DELETE | 删除资源 | `remove()` 删除任务 |

## 3. REST 最小概念

REST — 表现层状态转移 — 用“URL 表示资源 + HTTP 方法表示操作”的风格
GET    /tasks        → 查看所有任务
POST   /tasks        → 新建任务
GET    /tasks/1      → 查看 1 号任务
PUT    /tasks/1      → 更新 1 号任务
DELETE /tasks/1      → 删除 1 号任务

## 4. JSON 作为 API 数据格式

HTTP 请求体和响应体常用 JSON 传输数据。
例如创建任务时，POST 请求体可以是：
```json
{"title": "买牛奶", "done": false}

## 5. 与 CLI 项目对照
| CLI 操作 | HTTP 方法 + 路径 | 说明 |
|---|---|---|
| `tm.add("买牛奶")` | `POST /tasks` | 请求体 `{"title": "买牛奶"}` |
| `tm.show()` | `GET /tasks` | 返回任务列表 |
| `tm.remove(0)` | `DELETE /tasks/1` | 删除 1 号任务（索引 0 → 路径 1） |