import { useEffect, useState } from "react";
import DashboardLayout from "../layouts/DashboardLayout";
import { getDocuments } from "../services/api";
export default function HSN() {
    const [documents, setDocuments] = useState([]);
    const [search, setSearch] = useState("");
    const fetchDocuments = async () => {
        try {
            const data = await getDocuments();
            setDocuments(data);
        } catch (error) {
            console.log(error);
        }
    };
    useEffect(() => {
        fetchDocuments();
    }, []);
    const filteredDocuments = documents.filter((doc) => {
        return (
            doc.product?.toLowerCase().includes(
                search.toLowerCase()
            ) ||
            doc.category?.toLowerCase().includes(
                search.toLowerCase()
            ) ||
            doc.hsn_code?.toLowerCase().includes(
                search.toLowerCase()
            )
        );
    });
    const totalProducts = documents.length;
    const electronicsCount = documents.filter(
        doc => doc.category === "Electronics"
    ).length;
    const foodCount = documents.filter(
        doc => doc.category === "Food Grains"
    ).length;
    const unknownCount = documents.filter(
        doc => doc.category === "Unknown"
    ).length;
    return (
        <DashboardLayout>
            <div className="p-6">
       <h1 className="text-3xl font-bold mb-6">HSN Intelligence
            </h1>
        <input 
             type="text"
            placeholder="Search Product / Category / HSN"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full p-3 border rounded-lg mb-6"/>
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="bg-white p-6 rounded-xl shadow">
                <h2 className="text-lg font-semibold">
            Total Products
                </h2>
                <p className="text-3xl font-bold mt-4">{totalProducts}</p>
    </div>
            <div className="bg-white p-6 rounded-xl shadow">
            <h2 className="text-lg font-semibold">
                    Electronics</h2>
                <p className="text-3xl font-bold mt-4">{electronicsCount}</p>
            </div>
            <div className="bg-white p-6 rounded-xl shadow">
                <h2 className="text-lg font-semibold">
                    Food
                </h2>
                <p className="text-3xl font-bold mt-4">{foodCount}</p>
            </div>
            <div className="bg-white p-6 rounded-xl shadow">
                <h2 className="text-lg font-semibold">Unknown</h2>
            <p className="text-3xl font-bold mt-4">{unknownCount}</p>
        </div>
        </div>
            <div className="bg-white rounded-xl shadow overflow-x-auto">
        <table className="w-full">
            <thead className="bg-gray-100">
                <tr>
                <th className="p-4 text-left"> Product </th> 
                <th className="p-4 text-left"> Category </th>
                <th className="p-4 text-left"> HSN </th>
                <th className="p-4 text-left"> Product Code </th>
                <th className="p-4 text-left"> Country </th>
                </tr>
            </thead>
            <tbody>
{filteredDocuments.map((doc) => (
        <tr key={doc.id} className="border-t">
            <td className="p-4"> {doc.product} </td>
            <td className="p-4"> {doc.category} </td>
            <td className="p-4"> {doc.hsn_code} </td>
            <td className="p-4"> {doc.product_code} </td> 
            <td className="p-4"> {doc.country} </td>
            </tr>
        ))}
        </tbody>
        </table>
    </div>
    </div>
    </DashboardLayout>
    );
}