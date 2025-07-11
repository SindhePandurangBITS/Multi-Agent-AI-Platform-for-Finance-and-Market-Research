query1 = "List some recent milestones or developments for Goldman Sachs in US banking"
try:
    result = agent1.invoke({"input": query1})
    print(result['output'])
except Exception as e:
    print(f"Error executing agent: {str(e)}")
    try:
        result = agent1.run(query1)
        print(result)
    except Exception as e2:
        print(f"Error with run method: {str(e2)}")

response2 = "Exploring Use Cases of Generative AI in the BFSI Sector"
query2 = "Investigating AI Agents for Investment and Stock Market Applications in Financial Services"
result2 = agent1.invoke({"input": query2})
print(result2['output'])  

query3 = "Investigating AI Agents for Investment and Stock Market Applications in Financial Services"
result3 = agent1.invoke({"input": query3})
print(result3['output'])  
