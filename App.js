
import { Table } from 'antd';
import 'antd/dist/antd.min.css';
import './App.css';
import { columns } from './dataSource';
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [dataSource, setDataSource] = useState([]);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(false);


  useEffect(() => {
    fetchRecords(1);
  }, []);

  const fetchRecords = () => {
    axios
      .get(`http://127.0.0.1:5000/data/`)
      .then((res) => {
        setDataSource(res.data);
        setTotalPages(res.data.totalPages);
        setLoading(false);
        // setTotalPages(res.data.totalPages);
      });
  };

  return (

    // <><div className='App'>
    //   <Data/>
    // </div>
    <Table
    loading={loading}
    columns={columns}
    dataSource={dataSource}
    pagination={{
      pageSize: 10,
      total: totalPages,
      onChange: (page) => {
        fetchRecords(page);
      },
    }}
  ></Table>
  )
  
}

export default App;
