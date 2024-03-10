# cat_log_pt

Прототип сервиса загрузки каталогов из ресурсов.

## Как запустить?

### Зависимости
```
pip install fastapi
pip install uvicorn
pip install playwright
```
### Запуск
Запустить main.py

### Загрузка
```
fetch('http://127.0.0.1:8000/schedule_catalog_scheme_operation/bb8c681b-fc5f-49d3-817d-7d5f50e811e0', {method: 'POST'})
```
### Результат
```
http://127.0.0.1:8000/catalog_results/
```
