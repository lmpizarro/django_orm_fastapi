curl -X POST "http://localhost:5000/files/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "image=@README.md;type=text/plain" -F "params=@item.json;type=application/json"

echo 
curl -X POST "http://localhost:5000/job/" -H "Content-Type: application/json" -d '{"message":  "pepe", "index": 1}'

echo

curl -X POST "http://localhost:5000/uploadfile/"  -F 'image=@README.md;type=text/plain' -F 'id=1'

