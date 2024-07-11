# Hyper-Personalized-Home-Depot-Recommendation-Chatbot


## Introduction

In the digital age, personalization is key to enhancing customer experience and driving sales. This project focuses on developing a hyper-personalized recommendation chatbot for Home Depot using advanced AI techniques. Leveraging the Home Depot Products dataset from Kaggle, the chatbot will provide tailored product suggestions, thereby transforming customer interactions and boosting sales. The system is built using large language models (LLMs), chunking, sentence transformers, FAISS, GPT Turbo, and Streamlit.


<img width="1321" alt="Screenshot 2024-07-11 at 9 19 01 AM" src="https://github.com/Swati-Shiriyannavar/Hyper-Personalized-Home-Depot-Recommendation-Chatbot/assets/75442865/002d89f4-1124-4dd1-aa46-c0e90cf88aa9">

![image](https://github.com/Swati-Shiriyannavar/Hyper-Personalized-Home-Depot-Recommendation-Chatbot/assets/75442865/884ec0f6-1644-49bf-8ab8-48dba0c07b6a)

## Dataset Description

The Home Depot Products dataset, extracted by crawl feeds teams, includes the following columns:

- **index**: The index of the row
- **url**: The URL of the product
- **title**: The title of the product
- **images**: The images of the product
- **description**: The description of the product
- **product_id**: The product ID
- **sku**: The SKU of the product
- **gtin13**: The GTIN13 of the product
- **brand**: The brand of the product
- **price**: The price of the product
- **currency**: The currency of the product
- **availability**: The availability of the product
- **uniq_id**: The unique ID of the product
- **scraped_at**: The date the product was scraped

## Methodology

### Data Preprocessing

1. **Data Cleaning**: Handling missing values, correcting inconsistencies, and ensuring the dataset is ready for analysis.
2. **Feature Engineering**: Extracting relevant features from the dataset, such as product categories, price ranges, and brand popularity.

### Model Building

1. **Chunking and Embedding**: The dataset is chunked into manageable pieces. Each product description and related metadata are transformed into embeddings using a sentence transformer.
2. **FAISS Indexing**: The embeddings are indexed using FAISS (Facebook AI Similarity Search) to enable efficient and scalable similarity searches.
3. **GPT Turbo Integration**: GPT Turbo is used to generate natural language recommendations based on the user's preferences and search history.

### Chatbot Development

1. **Streamlit Interface**: A user-friendly interface is built using Streamlit, allowing users to interact with the chatbot seamlessly.
2. **Recommendation Engine**: The chatbot queries the FAISS index to find products similar to the user's preferences and presents them in a conversational manner.

### Tackling Hallucinations

To prevent the AI from generating inaccurate or irrelevant recommendations (a phenomenon known as hallucination), several strategies are implemented:

1. **Knowledge Base Verification**: Recommendations are cross-verified with a curated knowledge base to ensure accuracy.
2. **User Feedback Loop**: Users can provide feedback on recommendations, helping to refine and improve the model over time.
3. **Thresholding**: Setting confidence thresholds to ensure only high-confidence recommendations are presented to users.

## Benefits to the Organization

1. **Enhanced Customer Experience**: The chatbot provides personalized and relevant product suggestions, improving user satisfaction.
2. **Increased Sales**: By offering tailored recommendations, the likelihood of purchases increases, boosting overall sales.
3. **Operational Efficiency**: Automating the recommendation process reduces the need for extensive manual intervention, saving time and resources.

## Future Work

### Knowledge Graph Development

To further improve the accuracy and relevance of recommendations, future work will focus on developing a knowledge graph. This will involve:

1. **Entity Linking**: Connecting related entities (e.g., products, brands, categories) to provide a deeper understanding of the data.
2. **Semantic Enrichment**: Enhancing the dataset with additional semantic information to improve the quality of recommendations.
3. **Contextual Recommendations**: Utilizing the knowledge graph to offer more context-aware and nuanced recommendations.

## Conclusion

The development of a hyper-personalized Home Depot recommendation chatbot using advanced AI techniques presents significant benefits for enhancing customer experience and driving sales. By leveraging the Home Depot Products dataset and employing robust methodologies, the chatbot provides accurate and relevant product suggestions. Future enhancements, including the development of a knowledge graph, will further refine the system's capabilities, ensuring it remains a valuable tool for Home Depot and its customers.
