# Lesson 3-1. Introduction to APIs

## 1. What are APIs

### API: Application Programming Interface

An API is an *interface*. It's something that has been created to help two different systems interact with one another.

**A key idea** to remember is that *API functionality is defined independent of the actual implementation of the provider*. Essentially, you don't need to understand the entirety of the application implementation in order to interact with it through the API. This has multiple benefits:

1. It doesn't expose the implementation to those who shouldn't have access to it
2. The API provides a standard way of accessing the application
3. It makes it much easier to understand how to access the application's data

## 5. RESTful APIs

**REST** stands for *Representational State Transfer*, which is an architectural style introduced by [Roy Fielding in 2000](https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf).

Here's a short summary of the REST principles:

- **Uniform Interface**: Every rest architecture must have a standardized way of accessing and processing data resources. This include unique resource identifiers (i.e., unique URLs) and self-descriptive messages in the server response that describe how to process the representation (for instance JSON vs XML) of the data resource.
- **Stateless**: Every client request is self-contained in that the server doesn't need to store any application data in order to make subsequent requests
- **Client-Server**: There must be both a client and server in the architecture
- **Cacheable & Layered System**: Caching and layering increases networking efficiency
