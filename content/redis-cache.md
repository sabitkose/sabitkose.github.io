title: Distributed Caching With Redis And ASP.NET Core Minimal APIs
date: 2021-01-17 00:20
modified: 2021-01-17 00:20
author: Sabit
category: .Net
tags: .net, redis, docker, nuget, bogus
summary: How to make distributed caching with Redis And ASP.NET Core Minimal APIs.


In software, Some processes like IO and database sometimes could be slow. Data, image and file assets can access from the cache instead of the source too fast. Response time could be improved with cached data if data is likely to be reuse.

If multiple applications use the same source, local cache use causes some issues that have to figure out. That is, performance, scalability and consistency. Distributed cache use figures these issues out.

![Project Structure]({static}/images/cached-application.png)

# What is Redis?
> "Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker."

See also redis alternatives; MongoDB, Memcached, Hazelcast, Apache Cassandra, CouchBase etc.

# Installation and Dependencies

## Run Redis via Docker as a demo environment.
Redis endpoint is localhost:6379.
```
docker run --name demo-redis -p 6379:6379 -d redis

```

```
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED      STATUS      PORTS                                       NAMES      
1f776a7fadeb   redis     "docker-entrypoint.s…"   2 days ago   Up 2 days   0.0.0.0:6379->6379/tcp, :::6379->6379/tcp   demo-redis
```


## Install packages via Nuget, which is .Net package manager

```
dotnet add package Microsoft.Extensions.Caching.StackExchangeRedis
dotnet add package Microsoft.AspNetCore.Mvc.NewtonsoftJson
dotnet add package Bogus
```

## Create a empty .net core web app

```
mkdir project-name
dotnet new web

```
Created project structure.

![Project Structure]({static}/images/empty-dotnet-core-web-project-structure.png)


# Coding

There is simulation of a slow the database or IO process to get users in the demo. To get data faster, I cache users' data after the first access.

Open the Program.cs file.

## Create a data structure named User

```
public class User
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public string Email { get; set; }
}

```

```

using System.Text;
using Microsoft.Extensions.Caching.Distributed;
using Newtonsoft.Json;
using Bogus;

var builder = WebApplication.CreateBuilder(args);

// 1) Dependency Injection; Add and configure Redis cache service.
builder.Services.AddStackExchangeRedisCache(action => { action.Configuration = "localhost:6379"; });
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

// 2) Add a example APIs Method for demo.
app.MapGet("/users/{id}", async (http) =>
{
    // 3) Get an instance Redis cache service
    var _distributedCache = http.RequestServices.GetRequiredService<IDistributedCache>();

    // 4) set up variables for demo logic.
    IEnumerable<User> users;
    http.Request.RouteValues.TryGetValue("id", out var id);
    string json;
    string cacheKey = "users";
    
    // 5) If user data exists in Redis datastore, get users.
    var usersFromCache = await _distributedCache.GetAsync(cacheKey);
    if(usersFromCache != null)
    {
        json = Encoding.UTF8.GetString(usersFromCache);
        users = JsonConvert.DeserializeObject<List<User>>(json);
    }
    else
    {
        // 6) If user data doesn't exist in Redis datastore, simulate a slow database or IO process to get users. 
        // 6.1) Extra information for demo. Generate some dummy users via the Bogus package that creates mock data.
        Randomizer.Seed = new Random();
        int userIds = 0;
        var testUsers = new Faker<User>()
            .RuleFor(c => c.Id, f => userIds++)
            .RuleFor(c => c.FullName, (f, c) => f.Name.FullName())
            .RuleFor(c => c.Email, (f, c) => f.Internet.Email());
        users = testUsers.Generate(5000);

        // 7) Set users data as cached data in Redis.
        json = JsonConvert.SerializeObject(users);
        usersFromCache = Encoding.UTF8.GetBytes(json);
        var options = new DistributedCacheEntryOptions()
                        .SetSlidingExpiration(TimeSpan.FromDays(1)) 
                        .SetAbsoluteExpiration(DateTime.Now.AddMonths(1)); 
                await _distributedCache.SetAsync(cacheKey, usersFromCache, options);
    }

    var user = users.First(c => c.Id == int.Parse(id.ToString()));
    await http.Response.WriteAsJsonAsync(user);
});

app.Run();

```

# Results

Response time of the first request that is simulated slow process is **0,078000s**. The second request that Redis cache is **0,031000s**, As well as, Different apps can consume the same data via Redis. 
Redis can scale, and all apps show the same cached data.  

```
curl -o /dev/null -s -w "Total Time:  %{time_total}s\n" https://localhost:7241/users/3       
Total Time:  0,078000s

```

```
curl -o /dev/null -s -w "Total Time:  %{time_total}s\n" https://localhost:7241/users/3       
Total Time:  0,031000s

```


 
All the best!