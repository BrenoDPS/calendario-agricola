import { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([])

  useEffect(() => {
    async function fetchData() {
      console.log(import.meta.env.VITE_API_URL)
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}calendario`);
        if(!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        console
        setData(result);
      } catch (error) {
        console.error('Error fetching data: ', error);
      }
    }
    
    fetchData();
  }, []);

  return (
    <>
      Hello, World!
    </>
  )
}

export default App
