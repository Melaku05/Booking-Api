![](https://img.shields.io/badge/Microverse-blueviolet)

# Booking-Api

This app uses a Django, Django rest framework  as an API to send doctor details and appointment data to the frontend of a booking application.

Enjoy your API!


## Link to REACT FRONTEND

[REACT FRONTEND](https://github.com/Melaku05/booking-app-frontend)

## Built With

- python
- Django
- Django rest framework
- MYSQL
- Djoser 
- swagger


## Milestones

[Project Requirements](https://github.com/microverseinc/curriculum-final-capstone/blob/main/projects/business_requirements.md) - distributed into milestones below:

### Booking-app-backend

- [x] Milestone 1: Setup the project for backend (group task) 
- [x] Milestone 2: Implement (Djoser)devise gem
- [x] Milestone 3: Pytest test user
- [x] Milestone 4: Generate table and model for the Doctor 
- [x] Milestone 5: Generate table and model for the Reservation
- [x] Milestone 6: Pytest for Reservation 
- [x] Milestone 7: Pytest for Doctor
- [x] Milestone 8: Implement pytest
- [x] Milestone 9: Create Documentation

### Booking-app-frontend

- [x] Milestone 1: Setup the project for the frontend (group task)
- [x] Milestone 2: Node package manager dependencies (group task)
- [x] Milestone 3: Create login page (group task)
- [x] Milestone 4: Create navigation panel (group task)
- [x] Milestone 5: Create main page (Ranjit)
- [x] Milestone 6: Create details page (Melaku)
- [x] Milestone 7: Create Reservation page (Steve)
- [x] Milestone 8: Create my reservation page (Ismail)
- [x] Milestone 9: Create the redux store (group task)
- [x] Milestone 10: Create the doctor reducer (group task)
- [x] Milestone 11: Create the reservation reducer (group task)
- [x] Milestone 12: Create the login reducer (group task)

- [x] Debug linter errors

## API Endpoints

[Live server: Rswag api documentations]()

#### users/ endpoint

- GET /users/

  - Get the logged in user data
  - returns:

  ```
  {
    "id": 1,
    "username": "user",
    "created_at": "2022-08-28T21:31:51.962Z",
    "updated_at": "2022-08-28T21:31:51.962Z",
    "email": "user@email.com"
  }
  ```

- POST /users

  - Create a new user
  - e.g:

  ```
  {
    "username": "user",
    "email": "user@email.com",
    "password": "password"
  }
  ```

- DELETE /users/
  - Logged out the logged in user

#### doctors endpoint

- POST /doctors/

  - Create a new doctor
  - e.g:

  ```
  {
    "name": "Dr. doc",
    "detail": "Bio",
    "photo": "photo.jpg",
    "city": "London",
    "specialization": "Gynecologist",
    "fee": 100.00
  }
  ```

- GET /doctors/
  - Get all doctors
  - returns:
  ```
  [{
    "id": 1,
    "name": "Dr. doc",
    "detail": "Bio",
    "photo": "photo.jpg",
    "city": "London",
    "specialization": "Gynecologist",
    "fee": 100.0,
    "created_at": "2022-08-30T10:34:55.953Z",
    "updated_at": "2022-08-30T10:34:55.953Z"
  }]
  ```
- GET /doctors/:id

  - Get a doctor by id
  - returns:

  ```
  {
    "id": 1,
    "name": "Dr. doc",
    "detail": "Bio",
    "photo": "photo.jpg",
    "city": "London",
    "specialization": "Gynecologist",
    "fee": 100.0,
    "created_at": "2022-08-30T10:34:55.953Z",
    "updated_at": "2022-08-30T10:34:55.953Z"
  }
  ```

- DELETE /doctors/:id
  - Delete a doctor by id

#### reservations endpoint

- POST /reservations/

  - Create a new reservation
  - e.g:

  ```
  {
    "doctor_id": 1,
    "user_id": 1,
    "date": "2022-08-30",
    "city": "London",
  }
  ```

- GET /reservations/
  - Get all reservations
  - returns:
  ```
  [{
    "id": 1,
    "doctor_id": 1,
    "user_id": 1,
    "date": "2022-08-30",
    "city": "London",
    "created_at": "2022-08-30T10:34:55.953Z",
    "updated_at": "2022-08-30T10:34:55.953Z"
  }]
  ```
- GET /reservations/:id
  - Get a reservation by id
  - returns:
  ```
  {
    "id": 1,
    "doctor_id": 1,
    "user_id": 1,
    "date": "2022-08-30",
    "city": "London",
    "created_at": "2022-08-30T10:34:55.953Z",
    "updated_at": "2022-08-30T10:34:55.953Z"
  }
  ```

## Getting Started
### coming soon

## Usage
### coming soon

- Login into Booking App with your username
- Click on the list of Doctors to see their specific detailed information
- From Navigation or from details page click 'Reserve' to book an appointment
- Click from Navigation panel, 'My Reservation' to view a list of your appointment details

Enjoy saving time on long appointment calls by using our top ranking appointment booking App!

## Author 1:

👤 **Melaku Eshetu**

- GitHub: [Melaku05](https://github.com/Melaku05)
- Twitter: [Melaku](https://twitter.com/melaku_mel)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/melaku-eshetu/)

## Author 2:

👤 **Ranjit Luwang**

- GitHub: [@aboongm](https://github.com/aboongm)
- Twitter: [@John_luang1](https://twitter.com/John_luang1)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/aboongm)

## Author 3:

👤 **STEVE W DAMES JR**

- GitHub: [@githubhandle](https://github.com/steveWDamesJr)
- Twitter: [@twitterhandle](https://twitter.com/Steve88312331)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/steve-w-dames-jr/)

## Author 4:

👤 **Ismail Courr**

- GitHub: [@ismailco](https://github.com/ismailco)
- Twitter: [@ismailcourr](https://twitter.com/ismailcourr)
- LinkedIn: [Ismail courr](https://www.linkedin.com/in/ismailcourr)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Melaku05/Booking-Api/issues).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Hat tip to anyone whose code was used
- Original design idea by [Murat Korkmaz on Behance.]('https://www.behance.net/muratk')

## 📝 License

This project is [MIT](./MIT.md) licensed.
