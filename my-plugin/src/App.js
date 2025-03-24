import React, { useEffect, useState } from 'react';
import { Button, List, Table } from 'antd';
import axios from 'axios';

function App() {
    const [selectedVideos, setSelectedVideos] = useState([]);
    const [users, setUsers] = useState([]);
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        const handleMessage = (message) => {
            if (message.type === 'videoSelection') {
                const { videoId, isSelected } = message;
                if (isSelected) {
                    setSelectedVideos((prevVideos) => [...prevVideos, videoId]);
                } else {
                    setSelectedVideos((prevVideos) => prevVideos.filter((id) => id !== videoId));
                }
            }
        };

        chrome.runtime.onMessage.addListener(handleMessage);

        const fetchUsers = async () => {
            try {
                const response = await axios.get('http://your-aws-ec2-ip/api/user-management/');
                setUsers(response.data.users);
            } catch (error) {
                console.error(error);
            }
        };

        const fetchOrders = async () => {
            try {
                const response = await axios.get('http://your-aws-ec2-ip/api/order-list/');
                setOrders(response.data.orders);
            } catch (error) {
                console.error(error);
            }
        };

        fetchUsers();
        fetchOrders();

        return () => {
            chrome.runtime.onMessage.removeListener(handleMessage);
        };
    }, []);

    const handleRepost = () => {
        console.log('Selected videos for repost:', selectedVideos);
        // 这里可以添加转载逻辑
    };

    const userColumns = [
        {
            title: '用户名',
            dataIndex: 'username',
            key: 'username'
        },
        {
            title: '用户级别',
            dataIndex: 'user_level',
            key: 'user_level'
        },
        {
            title: '用户状态',
            dataIndex: 'user_status',
            key: 'user_status'
        },
        {
            title: '用户余额',
            dataIndex: 'user_balance',
            key: 'user_balance'
        }
    ];

    const orderColumns = [
        {
            title: '商品名称',
            dataIndex: 'product_name',
            key: 'product_name'
        },
        {
            title: '订单编号',
            dataIndex: 'order_number',
            key: 'order_number'
        },
        {
            title: '商户编号',
            dataIndex: 'merchant_number',
            key: 'merchant_number'
        },
        {
            title: '购买时间',
            dataIndex: 'purchase_time',
            key: 'purchase_time'
        },
        {
            title: '订单状态',
            dataIndex: 'order_status',
            key: 'order_status'
        },
        {
            title: '用户名',
            dataIndex: 'username',
            key: 'username'
        }
    ];

    return (
        <div>
            <List
                header={<div>Selected Videos</div>}
                bordered
                dataSource={selectedVideos}
                renderItem={(item) => <List.Item>{item}</List.Item>}
            />
            <Button onClick={handleRepost}>Repost Selected Videos</Button>
            <h2>用户管理列表</h2>
            <Table dataSource={users} columns={userColumns} />
            <h2>订单列表</h2>
            <Table dataSource={orders} columns={orderColumns} />
        </div>
    );
    const handleBindPlatform = async () => {
    try {
        const response = await axios.post('http://your-aws-ec2-ip/api/bind-platform/', {
            platform_name: 'TikTok',
            auth_token: 'your-auth-token'
        });
        console.log(response.data);
    } catch (error) {
        console.error(error);
    }
};

// 在返回的JSX中添加绑定按钮
<Button onClick={handleBindPlatform}>绑定平台账号</Button>

}

export default App;