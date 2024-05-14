# """
# Github Actions is automation tools used for automating testing tasks on every action we take.
# so, what github actions does is it tests and lints the code before pushing to above branch. if code fails then it will not push else it will push the code upwards.
# tests ran by github actions is defined by us in unit test,and sim linting is also provided by us by flake8 file.   
# """

# # so,here in our project we define workflows and jobs and jobs steps we perform in github action by github/workflow/checks.yml file.
# # by this checks.yml file github will perform tests and linting.

# # remeber there can be number of workflows and number if jobs in the workflows can be more. and each jobs can have single or multiple tests.


# # here is how we define github/workflow/checks.yml file

# # this --- are to defile thisis yml file.
# ---

# # name of workflow. this is what we will see in github actions.
# name: Checks

# # we need to add trigger.
# """
# trigger is something on which our workflows,jobs and stpes will be executed. 
# """
# # here we have added trigger. on keyword used to add trigger and whenever code is pushed to github repos
# # workflows,jobs ,stpes related to that trigger will be carried out
# on [push]

# # here we will be adding jobs that will do work
# jobs: 
#     # name of this job is defined by Test and Lint and it runs on ubuntu os
#     test-lint:
#         name: Test and Lint
#         runs-on: ubuntu-20.04
#     # steps are perfomed in this job
#         steps:
#             # name of this test is Login to dockerhub and its uses is to login to dockerhub 
#             - name: Login to Docker Hub
#             # this step is provided by github actions default.
#               uses: docker/login-action@v1
#               # when logging with dockerhub it will ask for username and token.
#               with:
#                 username: ${{ secrets.DOCKERHUB_USER }}
#                 password: ${{ secrets.DOCKERHUB_TOKEN }}
#             # this is used to get latest code from repositary to workflow.
#             - name: Checkout
#               uses: action/checkout@v2
#             # now here we will be performing testing by command by run: 
#             - name: Test
#               run: docker-compose run --rm app sh -c "python manage.py test"
#               # sim we will perform linting by command run:
#             - name: Lint
#               run: docker-compose run --rm app sh -c "flake8"
