# Deployment

This application was deployed on Heroku using Gunicorn as the Python web server. Django serves the website and AWS serves all our static and media assets. Here are the deployment steps:

**Pre-requisites:** Heroku account, Stripe account, AWS account

## Setting up Heroku

Create your Heroku account [here](https://signup.heroku.com/login).

Start off by cloning this project to your machine:

```Shell
git clone http://github.com/arlandfran/white_library.git
```

Next open a terminal and install Heroku CLI. Installation steps for each platform can be found in the official documentation [here](https://devcenter.heroku.com/articles/heroku-cli).

Once you've installed Heroku CLI run `heroku login` and follow the prompts.

Navigate to the project directory if you haven't already `cd white_library` and run `heroku create my-app-name`. Be sure to pass in your own unique app name such as "white-library-test" as white-library is already taken.

```bash
$ heroku create white-library-test
Creating ⬢ white-library-test... done
https://white-library-test.herokuapp.com/ | https://git.heroku.com/white-library-test.git
```

> By default the app is created in the US region, if you want to create the app in Europe provide the --region flag in the `heroku create` command.
>
> ```bash
> heroku create my-app-name --region eu
> ```

Once your Heroku app has been created, a git remote called `heroku` should also have been created and associated with your local git repository. You can confirm this by running `git remote -v`.

```bash
$ git remote -v
heroku  https://git.heroku.com/white-library-test.git (fetch)
heroku  https://git.heroku.com/white-library-test.git (push)
origin  http://github.com/arlandfran/white-library.git (fetch)
origin  http://github.com/arlandfran/white-library.git (push)
```

> Note: If you would like to setup automatic deployment on Heroku, you will need to have your own Github repository of this project, in which case you will need to fork this project and then connect that forked repository to Heroku.

```bash
$ git remote -v
heroku  https://git.heroku.com/white-library-test.git (fetch)
heroku  https://git.heroku.com/white-library-test.git (push)
origin  http://github.com/your-github-username/white-library.git (fetch)
origin  http://github.com/your-github-username/white-library.git (push)
```

At this stage you should be able to deploy your application to Heroku using `git push heroku main` and Heroku will automatically detect the language for your app is Python and configure the correct buildpack for the deployment. If you want to however manually set the buildpack you can do so by running these commands:

```bash
heroku buildpacks:set heroku/python
```

Now that your buildpacks have been configured correctly you can now setup AWS and connect it to Heroku.

## Setting up AWS

Create your AWS account [here](https://aws.amazon.com/) and click create an AWS account.

### S3 Configuration

Once you've created your account, sign into AWS as the root user and search for 'S3' by typing in the search bar or hitting `ALT+S` and select S3.

Under **Buckets** click create Create Bucket, choose a bucket name and select the closest region to you. For **Object Ownership** choose _ACLs enabled_ and ensure _Bucket owner preferred_ is selected. Finally, uncheck _Block all public access_, acknowledge allowing public settings and create the bucket, every other setting can be left as default.

Now that the bucket has been created, open the bucket and under the **Properties** tab, enable _Static Website Hosting_ and specify _index.html_ as the index document. Next go to the **Permissions** > **Bucket policy** (copy the Bucket ARN) > **Policy Generator** (this should open in a new tab).

Set the policy type to _S3 Bucket Policy_, type \* in the Principal field and select _GetObject_ under Actions. Paste the copied Bucket ARN into the ARN field and add the statement. Once the statement has been added, generate the policy and copy the generated policy. You can now close the tab, paste the generated policy into the policy editor and save your changes.

Now go back to **Permissions** > **Access Control List**. Check the List box for Everyone (public access), acknowledge these changes and save your changes.

The last thing you'll need to do now is setup the CORS configuration. Scroll to the bottom of the **Permissons** page and paste this configartion in the JSON editor:

```json
[
  {
    "AllowedHeaders": ["Authorization"],
    "AllowedMethods": ["GET"],
    "AllowedOrigins": ["*"],
    "ExposeHeaders": []
  }
]
```

### IAM Configuration

Search for 'IAM' by typing in the search bar or hitting `ALT+S` and select IAM.

Select **User Groups** located in sidebar and create a group. Choose a group name such as 'manage-white-library' and create the group.

After creating the group, select **Policies** located in the sidebar and create a policy. Select the JSON tab and import managed policy. Search for 'S3', select **AmazonS3FullAccess** and import the policy. Edit the resource object and include your copied Bucket ARN:

```json
"Resource": [
  "{your_bucket_arn}",
  "{your_bucket_arn}/*"
]
```

Review the policy, give it an appropriate name and description and create the policy.

Once you've created your policy, go back to **User Groups** > your created user group > **Permissions**. Expand the Add Permissions dropdown and select Attach policies. Search for your newly created policy and attach the policy.

The last thing you'll need to do now is add a user to your user group. In the sidebar select **Users** > Add users. Give the user an appropriate name, enable programmatic access and on the next page add your user to your user group.

Once your user has been created, download the CSV file that contains your user's Access key ID and Secret access key.

> **Important**: This is the only time the CSV will be available so please download the CSV.

### Connect to Heroku and upload Media folder

Now that AWS has been configured, we will need some set some Heroku environment variables so that the next time you deploy to Heroku, AWS will retrieve your static files and store them in a `static/` folder.

```bash
heroku config:set AWS_ACCESS_KEY_ID="your_access_key_id"
heroku config:set AWS_SECRET_ACCESS_KEY="your_secret_access_key"
```

You'll also need to set an `USE_AWS` environment variable as Django will be looking for this variable to determine whether to serve static files locally or from AWS.

```bash
heroku config:set USE_AWS="True"
```

Once these environment variables have been set and you have deployed to Heroku. On navigating to your S3 Bucket you will see that a `static/` folder now exists. Go ahead and create a folder called `media` and upload the files found [here](/media/), and under **Permissions**, grant public-read access.

With that AWS should be properly setup to serve your static and media files

## Running locally

**Pre-requisites:** Node, Python

To run this application locally clone the Github repository and install the node dependencies to enable ESlint for this project.

```bash
git clone http://github.com/arlandfran/white_library.git
cd white_library
npm install
```

Next create a virtual environment for the Python dependencies and install them in the virtual environment.

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

> venv\Scripts\activate.bat for Windows

Before you can run the app locally you'll need to set the local environment variables that Django needs to run.

```bash
# set VAR_NAME if using windows
export DEVELOPMENT=True
export SECRET_KEY=anythingyouwant
export STRIPE_PUBLIC_KEY=your_stripe_public_key
export STRIPE_SECRET_KEY=your_stripe_secret_key
export STRIPE_WH_SECRET=your_stripe_wh_secret
```
