# GraphQL Server Demo
This repository is a simple study I made about GraphQL and it works like a blog, where you can create users, posts and profiles.

I implemented the server using Node JS (Typescript) and Python. Both have the same functionalities and to help people that are not familiar with TypeScript or Python understand the whole thing, I programmed them using similar names and structures, which means that I might have violated a bunch of code conventions on this project. Please, keep that in mind.
Also, all implementations use Sqlite has a database. In fact, for convenience sake, both implementations point to the same database file.

# What is implemented
- Query
	- posts: Retrieves a list of Posts with pagination
	- me: Retrieves the profile of the logged user
	- users: Retrieves a paginated list of Users

- Mutation
	- postCreate: Creates a new post
	- postDelete: Deletes a post
	- signUp: Creates a user + user profile
	- signIn: User Login

# What's not implemented
- Mutation
	- postUpdate: If twitter don't have to let the user update it's posts, neither do I. ;) (Just kidding. Reason is same as the one bellow)
	- profileUpdate, userUpdate, userChangePassword, userDelete: I want to use this project to teach GraphQL to a couple devs, so those endpoints were left out on purpose.
	
- Subscription: The idea is to keep this example as simple as possible and a subscription would bring a level of complexity I don't want to approach right now.


# The N+1 problem, not solved here.
The goal here is to create a basic working example of GraphQL that can be easily upgradable, so I did not implement any dataloaders at the moment.
My plan is to, in the future, include the dataloaders and subscriptions.


# Server implementations
- server_nodejs: GraphQL implemented using NodeJS
- server_python: GraphQL implemented using Python


# Alternative, simpler server
I also made a simpler GraphQL server to use in a tutorial I made. (Link: https://raccoon.ninja/pt/dev-pt/tutorial-graphql-com-exemplos-graphql-python-nodejs-dev-tutorial/)
In this server, you can add/remove reviews for Products and do a couple of queries. To know more, please check the readme file inside the folder  ```simple_server_python```.
