# RAKUN TILCHI 

[![My Skills](https://skillicons.dev/icons?i=python,django,docker,postgres,flutter,react)](https://skillicons.dev) 

### 1. Login Endpoints 
<details>
<summary> 📌 POST /sign_up/ </summary>
  
### Sign Up Endpoint

> Request body:
```json
{
"name": "Firuz",
"login": "fjuraev",
"password": "Ewing0605",
"phone_number": "998953305830"
}
```
> Response (200)
```json
{
"message": "Successfully registered" 
}
```
</details>

<details>
<summary> 📌 GET /login/ </summary>
  
### Login endpoint
  

> Response (200): 
```json
{
 "user_id": 233
 "user_name": "Firuz Juraev"
}
```
</details>
<details>
<summary> 📌 POST /your_plans/ </summary>
  
### Your Plans endpoint
  
> Request body: 
```json
{
  "user_id": 2,
}
```

> Response (200): 
```json
{
 "plan_name": "English A1"
 "plan_image": "https//hafahfafhafjalfsk.jpg"
 "level": "A1"

}
```
</details>
