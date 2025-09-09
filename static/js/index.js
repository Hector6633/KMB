 // util: toast
    const showToast = (msg) => {
      const el = document.getElementById('toast');
      document.getElementById('toastBody').textContent = msg;
      const t = new bootstrap.Toast(el);
      t.show();
    };

    // Footer year
    document.getElementById('yr').textContent = new Date().getFullYear();

    // Populate time options for quick booking (every 30 min, 6:00–20:00)
    const qbTime = document.getElementById('qbTime');
    const times = [];
    for (let h = 6; h <= 20; h++) {
      for (let m of [0,30]) {
        const hh = String(h).padStart(2,'0');
        const mm = String(m).padStart(2,'0');
        times.push(`${hh}:${mm}`);
      }
    }
    qbTime.innerHTML = '<option value="">Select time</option>' + times.map(t=>`<option>${t}</option>`).join('');

    // Slot grid generator
    const slotGrid = document.getElementById('slotGrid');
    const slotStrings = ['06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30'];

    function renderSlots(bookedIdx = []){
      slotGrid.innerHTML = '';
      slotStrings.forEach((s, idx) => {
        const div = document.createElement('div');
        div.className = 'col-6 col-sm-4 col-md-3';
        const slot = document.createElement('div');
        slot.className = 'slot';
        slot.textContent = s;
        slot.dataset.status = bookedIdx.includes(idx) ? 'booked' : 'free';
        slot.addEventListener('click', () => {
          if (slot.dataset.status === 'booked') return;
          document.querySelectorAll('.slot[data-status="selected"]').forEach(el=>el.dataset.status='free');
          slot.dataset.status = 'selected';
          document.getElementById('selectedSlot').value = s;
        });
        div.appendChild(slot);
        slotGrid.appendChild(div);
      });
    }

    // Simulate availability based on date/pooja
    const poojaSelect = document.getElementById('pooja');
    const dateInput = document.getElementById('date');

    function updateAvailability(){
      // simple deterministic mock: book some indexes based on date + pooja hash
      const d = new Date(dateInput.value || new Date());
      const seed = d.getDate() + (poojaSelect.value || 'x').length;
      const booked = [];
      for (let i=0;i<slotStrings.length;i++){
        if ((i + seed) % 7 === 0) booked.push(i);
      }
      renderSlots(booked);
    }

    poojaSelect.addEventListener('change', updateAvailability);
    dateInput.addEventListener('change', updateAvailability);

    // Initialize defaults
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth()+1).padStart(2,'0');
    const dd = String(today.getDate()).padStart(2,'0');
    document.getElementById('qbDate').value = `${yyyy}-${mm}-${dd}`;
    document.getElementById('date').value = `${yyyy}-${mm}-${dd}`;
    updateAvailability();

    // Forms (mock submit)
    document.getElementById('bookingForm').addEventListener('submit', (e)=>{
      e.preventDefault();
      const slot = document.getElementById('selectedSlot').value;
      if (!slot) { showToast('Please select a slot.'); return; }
      showToast('Booking confirmed! Check your email for details.');
    });

    document.getElementById('quickBookingForm').addEventListener('submit', (e)=>{
      e.preventDefault();
      showToast('Quick booking placed! We\'ll confirm shortly.');
    });

    document.getElementById('contactForm').addEventListener('submit', (e)=>{
      e.preventDefault();
      showToast('Thank you! Your message has been sent.');
      e.target.reset();
    });

    document.getElementById('loginForm').addEventListener('submit', (e)=>{
      e.preventDefault();
      showToast('Logged in successfully (demo).');
    });

    document.getElementById('registerForm').addEventListener('submit', (e)=>{
      e.preventDefault();
      const p1 = document.getElementById('regPass').value;
      const p2 = document.getElementById('regPass2').value;
      if (p1 !== p2) { showToast('Passwords do not match.'); return; }
      showToast('Account created (demo).');
    });

    // Smooth scroll active link handling
    document.querySelectorAll('.nav-link').forEach(link=>{
      link.addEventListener('click', ()=>{
        document.querySelectorAll('.nav-link').forEach(l=>l.classList.remove('active'));
        link.classList.add('active');
      });
    });