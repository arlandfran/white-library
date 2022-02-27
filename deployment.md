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

At this stage you should be able to deploy your application to Heroku using `git push heroku main` and Heroku will automatically detect that our app is Python and configure the correct buildpack for the deployment. If you want to however manually set the buildpack you can do so by running these commands:

```bash
heroku buildpacks:set heroku/python
```

Now that your buildpacks have been configured correctly you can now setup setup AWS and connect it to Heroku.

## Setting up AWS

Create your AWS account [here](https://aws.amazon.com/) and click create an AWS account.

Once you've created your account, sign into AWS as the root user.

Once you're signed in, search for 'S3' by typing in the search bar or hitting `ALT+S` and select S3.

Under **Buckets** click create Create Bucket, choose a bucket name and select the closest region to you. For **Object Ownership** choose *ACLs enabled* and ensure *Bucket owner preferred* is selected. Finally, uncheck *Block all public access*, acknowledge allowing public settings and create the bucket, every other setting can be left as default.

Now that the bucket has been created, open the bucket and under the **Properties** tab, enable *Static Website Hosting* and specify *index.html* as the index document. Next go to the **Permissions** > **Bucket policy** (copy the Bucket ARN) > **Policy Generator** (this should open in a new tab).

Once your app has deployed you can run `heroku ps:scale web=1` command. This will start up 1 free dyno for your app to run on and you can visit your app with `heroku open`.

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
