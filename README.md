# manatel-test

## Getting Sdtarted
- If you have docker installed, run docker-compose up to get the database up and running
- CD into the backend/backend directory and run 'cp .env_example .env' to get default configurations
- Run server

## Comments and Time taken for Step 1
- Total time take approximately 40 mins
- Mostly due to setting up docker and pipenv
- Added code to prevent users from decreasing total students since that
would require a separate removing strategy for students

## Comments and Time taken for Step 2
- Total time take approximately 80 mins
- Mostly due to testing

## Comments and Time taken for Step 3
- Total time take approximately 60 mins
- Mostly due doing researching nested routers

## Bonus Tasks
- Added cusom migration to fake school and students
- Added django-filter backend
    - I can cretae custome filters but the project scope is too small for that
    - Added filters on StudentViewSet and StudentNestedViewSet