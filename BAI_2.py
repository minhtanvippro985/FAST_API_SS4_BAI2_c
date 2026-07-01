from fastapi import FastAPI
app = FastAPI()

orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]
status_list = ["pending" ,"paid","cancelled"]


@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    display_list = []
   
    if status not in status_list:
        return{
            "message" : "Trạng thái không hợp lệ"
        }

    for order in orders:
        if order['status'] == status:
            display_list.append(order)
    
    return {
        "message" : f"Danh sách đơn hàng {display_list}",
        "data" : display_list
     }
        


#khi gọi order/status/pending thì biến status sẽ nhận "pending"
# endpoint hiện tại có parameter những code viết chưa có chức năng lọc sản phẩm theo trạng thái , 
# hiện tại api đang hiện thị toàn bộ sản phẩm chứ không phải lọc
