from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from config import Config


class LLMService:
    def __init__(self, vector_store):
        self.llm=ChatOpenAI(temperature=0.7,
                            model_name='gpt-3.5-turbo',
                            openai_api_key=Config.OPEN_AI_KEY)
        

        self.memory=ConversationBufferMemory(
            memory_key="chat_history",
            return_message=True
        )

        self.chain=ConversationalRetrievalChain.fromllm(
            llm=self.llm,
            retriver=vector_store.vector_store.as_retrirver(),
            memory=self.memory
        )
    def get_responce(self,query):
        try:
            response=self.chain.invoke({"question":query})
            return response['answer']
        except Exception as e :
            print(f"Error getting LLm responce {e}")
            return "I encountered an error processing your request."
            