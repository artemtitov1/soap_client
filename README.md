# soap_client
Запустить веб-сервис  
В командной строке:  
pip install -r requirements.txt  
python main.py --addr http://localhost:52040/Library.asmx  
Выводится:  
![image](https://github.com/artemtitov1/soap_client/assets/113107946/69e35866-5933-45d4-80fd-4aee1c03838b)

Запросы осуществляются через LibraryServiceConnection.make_request(method),  
доступны методы get_all, get_by_id(id), get_by_title(title), delete_book(id), post_book(id, author, title, genre, price, publish_date, description)
