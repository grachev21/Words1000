import { useState, useEffect } from "react";
import axios from "axios";

const statusOptions = [
  { value: "unknown", label: "Неизвестно" },
  { value: "learning", label: "Изучаю" },
  { value: "repetition", label: "Повторяю" },
  { value: "learned", label: "Изучил" },
];

function OrdersList() {
  const [orders, setOrders] = useState([]);
  const [selectedStatuses, setSelectedStatuses] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchOrders = async () => {
    setLoading(true);

    let url = "http://127.0.0.1:8000/api/users/ListWord/";

    if (selectedStatuses.length > 0) {
      const params = new URLSearchParams();
      params.append("status_in", selectedStatuses.join(","));
      url += "?" + params.toString();
    }

    try {
      const token = localStorage.getItem("token");
      if (!token) {
        console.log("Токен не найден. Пожалуйста, войдите в систему.");
        setLoading(false);
        return;
      }
      const response = await axios.get(url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        }
      });
      // Если используешь пагинацию (PageNumberPagination), то обычно данные в .results
      setOrders(response.data.results || response.data);
    } catch (error) {
      console.error("Ошибка при загрузке заказов:", error);
    } finally {
      setLoading(false);
    }
  };

  // Загружаем данные при изменении выбранных статусов
  useEffect(() => {
    fetchOrders();
  }, [selectedStatuses]);

  const toggleStatus = (status) => {
    setSelectedStatuses(
      (prev) =>
        prev.includes(status)
          ? prev.filter((s) => s !== status) // убрать
          : [...prev, status], // добавить
    );
  };

  const resetFilters = () => {
    setSelectedStatuses([]);
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Фильтр по статусам</h2>

      {/* Кнопки-фильтры */}
      <div className="flex flex-wrap gap-2 mb-6">
        {statusOptions.map(({ value, label }) => (
          <button
            key={value}
            onClick={() => toggleStatus(value)}
            className={`px-5 py-2 rounded-lg text-sm font-medium transition-all ${
              selectedStatuses.includes(value)
                ? "bg-blue-600 text-white shadow-md"
                : "bg-gray-200 text-gray-700 hover:bg-gray-300"
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      {/* Кнопка сброса */}
      {selectedStatuses.length > 0 && (
        <button onClick={resetFilters} className="mb-6 text-red-600 hover:text-red-700 font-medium">
          Сбросить все фильтры
        </button>
      )}

      {/* Список заказов */}
      {loading ? (
        <p>Загрузка...</p>
      ) : (
        <div>
          {orders.length === 0 ? (
            <p className="text-gray-500">Заказы не найдены</p>
          ) : (
            <ul className="space-y-3">
              {orders.map((order) => (
                <li key={order.id} className="border rounded-lg p-4 bg-white shadow-sm">
                  <div className="flex justify-between">
                    <span className="font-semibold">Заказ #{order.id}</span>
                    <span
                      className={`px-3 py-1 rounded-full text-sm ${
                        order.status === "delivered"
                          ? "bg-green-100 text-green-700"
                          : order.status === "cancelled"
                            ? "bg-red-100 text-red-700"
                            : "bg-yellow-100 text-yellow-700"
                      }`}
                    >
                      {order.get_status_display || order.status}
                    </span>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}

export default OrdersList;
