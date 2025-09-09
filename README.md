# RAKUN TILCHI 

[![My Skills](https://skillicons.dev/icons?i=python,django,docker,postgres,flutter,react)](https://skillicons.dev) 

### 1. Login Endpoints 
<details>
<summary> 📌 POST /sign_up/ </summary>
  
### Login endpoint

> Request body: 
```json
{
"login": "umid",
"password": "umid0210" 
}
```

> Response (200): 
```json
{
 "user_id": 233
 "user_name": "Firuz Juraev"
}
```
</details>
<details>
<summary> 📌 PUT /edit_user/ </summary>
  
### Edit User Endpoint

> Request body: 
```json
{
"user_id": 4 
}
```

> Response (200): 
```json
{
 "user_id": 233,
 "user_name": "Firuz Juraev",
 "login": "fjuraev"
 "password": "ewing0506"
}
```
</details>



### 1. Plans Endpoints

<details>
<summary> 📌 GET /plans/ </summary>
  
### Plans Endpoint

> Response (200): 
```json
{
"1" { 
   "plan_id": 233,
   "plan_name": "English A1",
   "icon": "eng"
   "subscription": True }
"2" { 
   "plan_id": 123,
   "plan_name": "English A2",
   "icon": "eng"
   "subscription": False }
}
```
</details>

