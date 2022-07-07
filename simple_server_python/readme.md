# GraphQL Server Demo
This is a very simple server that I made as a demo of the basic functionalities of GraphQL.

# Schema
```
type Query {
    hello: String!
    myName(myNameIs: String!): String!
    reqCount: ReqCountPayload!
    products: [Product!]!
    review(reviewId: ID!): Review
    product(productId: ID!): Product
}

type Mutation {
    reviewCreate(newReviewData: ReviewCreateInput!): ReviewMutationPayload!
    reviewDelete(reviewId: ID!): ReviewMutationPayload!
}


type ReqCountPayload {
    count: Int!
    serverVersion: String!
}

type Product {
    id: ID!
    name: String!
    price: Float!
    reviews: [Review!]!
}

type Review {
    id: ID!
    author: String!
    content: String!
    grade: Int!
    product: Product!
    dateAdded: String!
}

type ReviewMutationPayload {
    success: Boolean!
    errorMessage: String
    review: Review
}

input ReviewCreateInput {
    productId: ID!
    author: String!
    grade: Int!
    content: String!
}
``` 

# Install
Install the dependencies:
```shell
pip install -r requirements.txt
```

# Running the server
```shell
python app.py
```