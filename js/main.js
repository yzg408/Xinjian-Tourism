/* ============================================
   新建大观 · 全域智慧文旅平台
   主交互脚本
   ============================================ */

// ===== 导航栏滚动效果 =====
const header = document.querySelector('.header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  if (scrollY > 80) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
  lastScroll = scrollY;
});

// ===== 移动端菜单 =====
const menuToggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
const navOverlay = document.querySelector('.nav-overlay');

function toggleMenu() {
  menuToggle.classList.toggle('active');
  nav.classList.toggle('open');
  if (navOverlay) navOverlay.classList.toggle('open');
  document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
}

if (menuToggle) {
  menuToggle.addEventListener('click', toggleMenu);
}

if (navOverlay) {
  navOverlay.addEventListener('click', toggleMenu);
}

// 点导航链接后关菜单
document.querySelectorAll('.nav a').forEach(link => {
  link.addEventListener('click', () => {
    if (nav.classList.contains('open')) toggleMenu();
  });
});

// ===== 当前页面高亮 =====
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav a').forEach(link => {
  const href = link.getAttribute('href');
  if (href === currentPage) {
    link.classList.add('active');
  }
});

// ===== 视差滚动效果（首页英雄区） =====
const hero = document.querySelector('.hero');
if (hero) {
  window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    const heroHeight = hero.offsetHeight;
    if (scrollY <= heroHeight) {
      const progress = scrollY / heroHeight;
      const content = hero.querySelector('.hero-content');
      const overlay = hero.querySelector('.hero-overlay');
      if (content) {
        content.style.transform = `translateY(${progress * 60}px)`;
        content.style.opacity = 1 - progress * 1.2;
      }
    }
  });
}

// ===== 标签选择器（路线定制页） =====
document.querySelectorAll('.tag-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    btn.classList.toggle('active');
    // 触发生成推荐
    const activeTags = [...document.querySelectorAll('.tag-btn.active')]
      .map(b => b.dataset.tag);
    generateRecommendations(activeTags);
  });
});

function generateRecommendations(tags) {
  const routes = window.routeData || [];
  const container = document.querySelector('.recommended-routes');
  if (!container) return;

  if (tags.length === 0) {
    // 显示所有路线
    renderRoutes(container, routes);
    return;
  }

  const matched = routes.filter(route =>
    route.tags.some(tag => tags.includes(tag))
  );
  renderRoutes(container, matched.length > 0 ? matched : routes);
}

function renderRoutes(container, routes) {
  container.innerHTML = routes.map(route => `
    <div class="route-card">
      <div class="route-image" style="background: linear-gradient(135deg, ${route.bgFrom}, ${route.bgTo});">
        <span class="route-tag" style="background: ${route.tagColor};">
          ⏱ ${route.duration}
        </span>
        <span style="font-size: 3rem; opacity: 0.6;">${route.emoji}</span>
      </div>
      <div class="route-body">
        <h3>${route.title}</h3>
        <p>${route.description}</p>
        <div class="route-stops">
          ${route.stops.map((stop, i) => `
            <div class="route-stop">
              <div class="route-stop-icon" style="background: ${stop.color}; color: #fff;">
                ${stop.icon}
              </div>
              <span>${stop.name}</span>
              ${stop.type === '美食' || stop.type === '住宿' ? `<span style="margin-left: auto; font-size: 0.75rem; color: var(--text-light); padding: 0.1rem 0.5rem; background: rgba(201,168,76,0.1); border-radius: 50px;">${stop.type}</span>` : ''}
            </div>
          `).join('')}
        </div>
        <a href="#" class="feature-link">查看详情 →</a>
      </div>
    </div>
  `).join('');
}

// ===== 路线数据 =====
window.routeData = [
  {
    title: '探寻大汉风云',
    description: '穿越千年，感受海昏侯的辉煌与汪山土库的赣派建筑之美。',
    duration: '1日游',
    emoji: '🏛️',
    bgFrom: '#C9A84C', bgTo: '#A8883A',
    tagColor: '#C9A84C',
    tags: ['历史', '文化', '汉韵'],
    stops: [
      { name: '海昏侯国遗址公园', icon: '👑', type: '景点', color: '#C9A84C' },
      { name: '汪山土库', icon: '🏘️', type: '景点', color: '#A8883A' },
      { name: '大塘东坡肉', icon: '🍖', type: '美食', color: '#E8734A' },
    ]
  },
  {
    title: '品味赣鄱风情',
    description: '在南矶山观万鸟齐飞，在厚田沙漠体验极限越野。',
    duration: '2日游',
    emoji: '🦅',
    bgFrom: '#2E86AB', bgTo: '#1B5E7A',
    tagColor: '#2E86AB',
    tags: ['自然', '户外', '亲子'],
    stops: [
      { name: '南矶山湿地观鸟', icon: '🦩', type: '景点', color: '#2E86AB' },
      { name: '厚田沙漠越野', icon: '🏜️', type: '景点', color: '#E8734A' },
      { name: '沙漠星空露营', icon: '⛺', type: '住宿', color: '#6B5E4A' },
    ]
  },
  {
    title: '祈福寻根问祖',
    description: '登西山万寿宫祈福，访梦山古迹，感受赣鄱人文底蕴。',
    duration: '1日游',
    emoji: '🙏',
    bgFrom: '#8B5CF6', bgTo: '#6D28D9',
    tagColor: '#8B5CF6',
    tags: ['文化', '祈福', '亲子'],
    stops: [
      { name: '西山万寿宫', icon: '🏯', type: '景点', color: '#8B5CF6' },
      { name: '梦山风景区', icon: '⛰️', type: '景点', color: '#6D28D9' },
      { name: '周边特色民宿', icon: '🏡', type: '住宿', color: '#C9A84C' },
    ]
  },
  {
    title: '亲子趣玩之旅',
    description: '寓教于乐，让孩子们在游玩中了解历史文化与自然生态。',
    duration: '2日游',
    emoji: '👨‍👩‍👧‍👦',
    bgFrom: '#F59E0B', bgTo: '#D97706',
    tagColor: '#F59E0B',
    tags: ['亲子', '自然', '户外'],
    stops: [
      { name: '海昏侯考古体验', icon: '🔍', type: '景点', color: '#C9A84C' },
      { name: '南矶山自然课堂', icon: '📖', type: '景点', color: '#2E86AB' },
      { name: '厚田沙漠滑沙', icon: '🏂', type: '景点', color: '#F59E0B' },
      { name: '亲子民宿套餐', icon: '🛌', type: '住宿', color: '#E8734A' },
    ]
  },
  {
    title: '汉韵国潮深度游',
    description: '穿上汉服，沉浸式体验汉代文化的魅力。',
    duration: '2日游',
    emoji: '🎎',
    bgFrom: '#C9A84C', bgTo: '#8B5CF6',
    tagColor: '#8B5CF6',
    tags: ['历史', '文化', '汉韵'],
    stops: [
      { name: '海昏侯国遗址（汉服专场）', icon: '👘', type: '景点', color: '#C9A84C' },
      { name: '汪山土库《程府风云》剧本杀', icon: '🎭', type: '景点', color: '#8B5CF6' },
      { name: '万寿宫非遗夜市', icon: '🏮', type: '美食', color: '#E8734A' },
      { name: '汉韵主题民宿', icon: '🏮', type: '住宿', color: '#C9A84C' },
    ]
  },
  {
    title: '摄影采风之旅',
    description: '捕捉新建最美瞬间，从湿地候鸟到沙漠星空。',
    duration: '3日游',
    emoji: '📷',
    bgFrom: '#2E86AB', bgTo: '#E8734A',
    tagColor: '#2E86AB',
    tags: ['自然', '户外', '摄影'],
    stops: [
      { name: '南矶山湿地日出', icon: '🌅', type: '景点', color: '#2E86AB' },
      { name: '厚田沙漠日落', icon: '🌄', type: '景点', color: '#E8734A' },
      { name: '海昏侯博物馆文物摄影', icon: '📸', type: '景点', color: '#C9A84C' },
      { name: '星空摄影基地', icon: '🌌', type: '住宿', color: '#6B5E4A' },
    ]
  }
];

// ===== 滚动动画 (Intersection Observer) =====
const animateOnScroll = () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

  document.querySelectorAll('.animate-in').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
    observer.observe(el);
  });
};

// 等 DOM 加载完
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', animateOnScroll);
} else {
  animateOnScroll();
}

// ===== 倒计时（用于节日活动页） =====
function initCountdown(targetDate, elementId) {
  const el = document.getElementById(elementId);
  if (!el) return;

  function update() {
    const now = new Date();
    const target = new Date(targetDate);
    const diff = target - now;

    if (diff <= 0) {
      el.innerHTML = '🎉 正在进行中！';
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

    el.innerHTML = `<span class="countdown-num">${days}</span>天 <span class="countdown-num">${hours}</span>时 <span class="countdown-num">${minutes}</span>分`;
  }

  update();
  setInterval(update, 60000);
}
