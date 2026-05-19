/* ============================================
   新建大观 · API 数据访问层
   ============================================ */

const API_BASE = 'http://localhost:8001/api';

const api = {
  async get(path) {
    const res = await fetch(`${API_BASE}${path}`);
    if (!res.ok) throw new Error(`API ${res.status}: ${res.statusText}`);
    return res.json();
  },

  async post(path, data) {
    const res = await fetch(`${API_BASE}${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error(`API POST ${res.status}: ${res.statusText}`);
    return res.json();
  },

  // ===== 景点 =====
  async getSpots(params = {}) {
    const q = new URLSearchParams(params).toString();
    return this.get(`/scenic-spots${q ? '?' + q : ''}`);
  },

  async getSpot(id) {
    return this.get(`/scenic-spots/${id}`);
  },

  async getCategories() {
    return this.get('/scenic-spots/categories');
  },

  // ===== 路线 =====
  async getRoutes(params = {}) {
    const q = new URLSearchParams(params).toString();
    return this.get(`/routes${q ? '?' + q : ''}`);
  },

  async getRoute(id) {
    return this.get(`/routes/${id}`);
  },

  // ===== 节日 =====
  async getFestivals(params = {}) {
    const q = new URLSearchParams(params).toString();
    return this.get(`/festivals${q ? '?' + q : ''}`);
  },

  async getFestival(id) {
    return this.get(`/festivals/${id}`);
  },

  // ===== 反馈 =====
  async submitFeedback(data) {
    return this.post('/feedback', data);
  },

  // ===== 定制旅程 =====
  async submitTourPlan(data) {
    return this.post('/tour-plans', data);
  },

  // ===== 统计 =====
  async getStats() {
    return this.get('/stats');
  },

  // ===== 健康检查 =====
  async health() {
    return this.get('/health');
  },
};
