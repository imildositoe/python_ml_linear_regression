### To fulfill the version control part, we follow the steps below (these commands are performed in the command line): 

1. Clone the repository to my local directory using the repository link (this is the actual link of the project):
   ```bash
   git clone https://github.com/imildositoe/python_ml_linear_regression_task.git
   ```

2. Change the directory to the just cloned repository (the directory will have the name of the repository):
   ```bash
   cd python_ml_linear_regression_task
   ```

3. Access the team branch by switching to the develop branch:
   ```bash
   git checkout develop
   ```

4. Create a new branch called my_dev_branch and switch to it to store my modifications: 
   ```bash
   git checkout -b my_dev_branch
   ```

5. After the changes, I stage them for commit:
   ```bash
   git add .
   ```

6. Commit my changes with a message that describes them:
   ```bash
   git commit -m "New function added."
   ```

7. Push my changes to my "my_dev_brach" branch: 
   ```bash
   git push -u origin my_dev_branch
   ```

8. After pushing the changes to my_dev_branch, I create a pull request on the remote repository GitHub website. Then I wait for my team to provide feedback and make necessary amendments to the branch. 

9. After the modifications, I push my changes again to the my_dev_branch:
   ```bash
   git push -u origin my_dev_branch
   ```

10. After the approval of the modifications in my_dev_branch, the repository owner merges them into the develop branch.

11. After the merge has been performed, I pull the develop branch fully updated:
   ```bash
   git checkout develop
   git pull origin develop
   ```