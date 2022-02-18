
import { Table } from 'antd';
import 'antd/dist/antd.min.css';
import { columns } from './dataSource';
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [dataSource, setDataSource] = useState([]);
  // const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    fetchRecords(1);
  }, []);

  const fetchRecords = () => {
    // setLoading(true);
    axios
      .get(`http://127.0.0.1:5000/data/`)
      .then((res) => {
        setDataSource(res.data);
        // setTotalPages(res.data.totalPages);
      });
  };

    // const fetchRecords = () => {
    //   fetch('http://127.0.0.1:5000/data/').then(res=> {
    //       res.json().then(response => {
    //         console.log(response)
    //       });
    //     }
    //   );
    // };

  return (

    <Table dataSource={dataSource} columns={columns} pagination={false} />
  )
  
}

export default App;
