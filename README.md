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
<summary> 📌 POST /login/ </summary>
  
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
<summary> 📌 GET /your_plans/ </summary>
  
### Your Plans endpoint
  

> Response (200): 
```json
{
 "plan_name": "English A1"
 "plan_image": "https//hafahfafhafjalfsk.jpg"
 "level": "A1"

}
```
</details>
