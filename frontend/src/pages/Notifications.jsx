import DashboardLayout from "../layouts/DashboardLayout";
export default function Notifications() {
    const notifications =
        JSON.parse(
            localStorage.getItem(
                "notifications"
            )
        ) || [];
    return (
        <DashboardLayout>
    <div className="p-6">
        <h1 className="text-3xl font-bold mb-6">Notifications</h1>
    <div className="space-y-4">{
            notifications.length === 0 ? (
        <div className="bg-white p-6 rounded-2xl shadow">
        No Notifications Yet
        </div>
    ) : (
notifications.map((item) => (
            <div
                key={item.id}
            className="bg-white p-5 rounded-2xl shadow"                                >
            <div className="flex justify-between">
                <div>
            <h2 className="font-bold">{item.invoice}</h2>
            <p className="text-gray-600 mt-2">{item.message}</p>
            </div>
                <p className="text-sm text-gray-400">{item.time}</p>
                </div>
            </div>
        )))}
    </div>
</div>
        </DashboardLayout>
    );
}