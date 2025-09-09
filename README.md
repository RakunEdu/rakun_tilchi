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



### 2. Plans Endpoints

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



<details>
<summary> 📌 POST /get_plan_questions/ </summary>
  
### Get Plan Questions Endpoint

> Request
```json
{
  "plan_id": 23 
}

```


> Response (200): 
```json
{
"1" { 
   "word": "bear",
   "translation": "ayiq"}
"2" { 
   "word": "cat",
   "translation": "mushuk"}
... 
"300" { 
   "word": "forest",
   "translation": "o'rmon"}
}
```
</details>


### 3. Game History Endpoints 
<details>
<summary> 📌 GET /game_histories/ </summary>
  
### Game Histories Endpoint

> Response (200): 
```json
{
"1" { 
   "game_id": 233,
   "game_date": "01.12.2025",
   "end_time": "14:56"
   "plan_name": "English A1", 
   "players": [{"player_name": "Umid", "accuracy": "96", "score": "45/47", "winner": True},
               {"player_name": "Firuz", "accuracy": "93", "score": "41/44", "winner": False}] 

}
"2" { 
   "game_id": 300,
   "game_date": "21.12.2025",
   "end_time": "18:56"
   "plan_name": "English A2", 
   "players": [{"player_name": "Asil", "accuracy": "89", "score": "40/45", "winner": True},
               {"player_name": "Norboy", "accuracy": "88", "score": "39/44", "winner": False}] 
}
```
</details>



<details>
<summary> 📌 POST /save_game_history/ </summary>
  
### Save Game History Endpoint

> Request: 
```json
{
"game_date": "01.12.2025",
"end_time": "14:56"
"plan_id": 21, 
"players": [{"player_name": "Umid", "accuracy": "96", "score": "45/47", "winner": True},
            {"player_name": "Firuz", "accuracy": "93", "score": "41/44", "winner": False}] 

```

> Response (200): 
```json
{
 "message": "Saved successfully"
}
```

</details>



